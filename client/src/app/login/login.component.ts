import { Component } from '@angular/core'
import { AuthenticationService } from '../authentication.service'
import {TokenPayload} from '../token-payload'
import { Router } from '@angular/router'

@Component({
  templateUrl: './login.component.html'
})
export class LoginComponent {
  credentials: TokenPayload = {
    username: '',
    email: '',
    password: ''
  }
  dummycredentials:TokenPayload={
    username: 'abc',
    email: 'abc@gmail.com',
    password: '123456'
  }

  constructor(private auth: AuthenticationService, private router: Router) {}

  login() {
    this.auth.login(this.credentials).subscribe(
      (data) => {
        console.log(data)
        if(data['token'])
        this.router.navigateByUrl('/')
        else
        window.alert("invalid username or password")
      },
      (err) => {
        console.log(err)
        window.alert("invalid username or password")
      }
    )
  }
}
