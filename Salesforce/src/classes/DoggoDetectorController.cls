public with sharing class DoggoDetectorController {
	public static Map<String,Map<String, String>> dogTypeToDescription = new Map<String, Map<String, String>>{
		'Labrador Retriver' => new Map<String, String>{
			'name' => 'Labrador Retriver',
			'life' => '10 do 12 lat',
			'whereFrom' => 'Nowa Fundlandia',
			'character' => ' Inteligentny, Towarzyski, Zrównoważony, Miły, Zwinny, Ufny, Łagodny',
			'size' => 'Samiec: 57–62 cm, Samica: 55–60 cm',
			'color' => 'Barwa czarna, Czekoladowy, Żółty'
		}
	};

	@AuraEnabled
	public static Map<String,String> getDogInfo(String base64, String filename) {
		ContentVersion cv = createContentVersion(base64, filename);
		ContentDocumentLink cdl = createContentLink(cv.Id);
		ContentDistribution cd = createContentDistribution(cv.Id);
		String link = [SELECT DistributionPublicUrl FROM ContentDistribution WHERE Id =: cd.Id].DistributionPublicUrl;
		return getPrediction(link);
	}

	private static ContentVersion createContentVersion(String base64, String filename) {
		ContentVersion cv = new ContentVersion();
		cv.VersionData = EncodingUtil.base64Decode(base64);
		cv.Title = filename;
		cv.PathOnClient = filename;
		try {
			insert cv;
			return cv;
		} catch(DMLException e) {
			System.debug(e);
			return null;
		}
	}

	private static ContentDocumentLink createContentLink(String contentVersionId) {
		Id recordId = [SELECT Id FROM Contact LIMIT 1].Id;
		if (contentVersionId == null) { return null; }
		ContentDocumentLink cdl = new ContentDocumentLink();
		cdl.ContentDocumentId = [
			SELECT ContentDocumentId
			FROM ContentVersion
			WHERE Id =: contentVersionId
		].ContentDocumentId;
		cdl.LinkedEntityId = recordId;
		cdl.ShareType = 'V';
		try {
			insert cdl;
			return cdl;
		} catch(DMLException e) {
			System.debug(e);
			return null;
		}
	}

	private static ContentDistribution createContentDistribution (String contentVersionId) {
		ContentDistribution cd = new ContentDistribution();
		cd.Name = 'Test';
		cd.ContentVersionId = contentVersionId;
		cd.PreferencesAllowViewInBrowser= true;
		cd.PreferencesLinkLatestVersion=true;
		cd.PreferencesNotifyOnVisit=false;
		cd.PreferencesPasswordRequired=false;
		cd.PreferencesAllowOriginalDownload= true;
		insert cd;
		return cd;
	}

	public static Map<String,String> getPrediction (String pictureUrl) {

		HttpRequest req = new HttpRequest();
		req.setEndpoint('callout:doggoDetector' + pictureUrl);
		req.setMethod('GET');

		HTTPResponse res = new Http().send(req);
		String dogType = res.getBody();
		return dogTypeToDescription.get(dogType);
	}

}