import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../authentication.service'
import { Router } from '@angular/router'
@Component({
  selector: 'app-newpost',
  templateUrl: './newpost.component.html',
  styleUrls: ['./newpost.component.css']
})
export class NewpostComponent implements OnInit {
  post={
    title:'',
    content:'',
    email:''
  }
  constructor(private router: Router,private auth: AuthenticationService) { }


  ngOnInit(): void {
  }

  add() {
    this.auth.addnewpost(this.post).subscribe(
      (message) => {
        this.router.navigateByUrl("/")
      },
      err => {
        console.error(err)
      }
    )
  }
}
