import { Component } from '@angular/core';
import {User} from './user';
import {RegistrationService} from './registration.service'


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'tdf';
  constructor(private registeri:RegistrationService){}

   usr=new User("","","","");


   onSubmit(){

     this.registeri.register(this.usr)
            .subscribe((data)=>{console.log("success",data)
          
            this.success()
          
          
          
          } ,error=>console.log('Error!',error))
   }

   success(){
     console.log("hurray!!!!")
     
   }
  }


