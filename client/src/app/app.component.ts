import { Component } from '@angular/core'
import { AuthenticationService } from './authentication.service'

import { Router } from '@angular/router';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  title='client';
  constructor(private router: Router,public auth :AuthenticationService) { }



}
