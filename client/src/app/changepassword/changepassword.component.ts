import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '../authentication.service';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-changepassword',
  templateUrl: './changepassword.component.html',
  styleUrls: ['./changepassword.component.css']
})
export class ChangepasswordComponent implements OnInit {

   constructor(private auth: AuthenticationService, private router: Router,private route : ActivatedRoute) {
  }
token:string
  user = {
    password : ''
};

  ngOnInit(): void {
    const  token= this.route.snapshot.paramMap.get('token');
    this.token=token;

  }

  change() {
    this.auth.change(this.user.password,this.token)
      .subscribe(data => {
       
        window.alert('Password changed successfully');
        this.router.navigateByUrl('/login');
      }, error => {
        console.log(error)
        window.alert('Time expired');
      });
  }

}
