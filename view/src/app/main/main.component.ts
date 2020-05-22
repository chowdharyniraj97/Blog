import { Component, OnInit } from '@angular/core';
import { FlaskapiService } from "../flaskserviceapi.service";
import { Subscription } from 'rxjs';
import { Post } from "../models/Post";


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private flaskApiService: FlaskapiService) { }
  public posts: Post;
  public postsSubscription: Subscription

  public getPosts(){
    this.postsSubscription = this.flaskApiService.getPosts().subscribe(p => {
      console.log(p)
      this.posts=p
      // this.posts = p["data"];
      // console.log(this.posts)
    })
  }
  ngOnInit(): void {
    this.getPosts();
  }

}
