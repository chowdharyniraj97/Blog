import { Component } from '@angular/core'
import { AuthenticationService } from '../authentication.service'
import { UserDetails} from '../user-details'
@Component({
  templateUrl: './profile.component.html'
})
export class ProfileComponent {
  details: UserDetails

  constructor(private auth: AuthenticationService) {}

  ngOnInit() {
    this.details = this.auth.getUserDetails()
    console.log(this.details['identity'].username)
  }
}