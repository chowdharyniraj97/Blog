import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../authentication.service'
import {Posts} from '../posts'
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  post:Posts
  constructor(public auth:AuthenticationService) { }
  public getPosts(){
    this.auth.getPosts().subscribe(p => {
      this.post=p
      // this.posts = p["data"];
      // console.log(this.posts)
    })
  }
  ngOnInit(): void {
   this.getPosts()
  }

}
