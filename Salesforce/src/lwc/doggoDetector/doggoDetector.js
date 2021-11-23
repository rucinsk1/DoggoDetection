import { LightningElement } from 'lwc';

import getDogInfo from '@salesforce/apex/DoggoDetectorController.getDogInfo';

export default class DoggoDetector extends LightningElement {

    doggoSearched = false;
    isSpinner = false;

    dog;

    name;
    life;
    whereFrom;
    character;
    size;
    color;

    handleUploadFinished (event) {
        const file = event.target.files[0]
        var reader = new FileReader()
        reader.onload = () => {
            var base64 = reader.result.split(',')[1]
            this.fileData = {
                'filename': file.name,
                'base64': base64
            }
        }
        reader.readAsDataURL(file)
    }

    handleSearchDoggo () {
        this.isSpinner = true;
        const {base64, filename} = this.fileData
        getDogInfo({ base64, filename }).then(result => {
            this.dog = JSON.parse(JSON.stringify(result))
            this.name = this.dog.name;
            this.life = this.dog.life;
            this.whereFrom = this.dog.whereFrom;
            this.character = this.dog.character;
            this.size = this.dog.size;
            this.color = this.dog.color;

            this.isSpinner = false
            this.doggoSearched = true;
        })
    }
}