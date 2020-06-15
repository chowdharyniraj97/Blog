import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '../authentication.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {
  // tslint:disable-next-line:variable-name

  constructor(private auth: AuthenticationService, private router: Router) {
  }

user = {
    email : ''
};

  ngOnInit(): void {

  }

  reset() {
    this.auth.reset(this.user)
      .subscribe(data => {
        window.alert('Email has been sent to reset');
      }, error => {
        window.alert('illegal email');
      });
  }
}
