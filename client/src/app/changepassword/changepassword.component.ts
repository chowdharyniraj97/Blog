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
email:string
  user = {
    password : ''
};

  ngOnInit(): void {
    const  email= this.route.snapshot.paramMap.get('email');
    this.email=email;

  }

  change() {
    this.auth.change(this.user.password,this.email)
      .subscribe(data => {
        window.alert('Password changed successfully');
        this.router.navigateByUrl('/login');
      }, error => {
        window.alert('Time expired');
      });
  }

}
