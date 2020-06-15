import { Component } from '@angular/core'
import { AuthenticationService } from '../authentication.service'
import { Router } from '@angular/router'
import {TokenPayload} from '../token-payload'

@Component({
  templateUrl: './register.component.html'
})
export class RegisterComponent {
  credentials: TokenPayload = {
    username:'',
    email: '',
    password: ''
  }

  constructor(private auth: AuthenticationService, private router: Router) {}

  register() {
    this.auth.register(this.credentials).subscribe(
      () => {
        this.router.navigateByUrl('/login')
      },
      err => {
        console.error(err)
      }
    )
  }
}