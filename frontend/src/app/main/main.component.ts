import { Component, OnInit, OnDestroy } from '@angular/core';
import { FlaskapiService } from "../flaskapi.service";
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit, OnDestroy {

  constructor(private flaskApiService: FlaskapiService) { }
  public posts: any[];
  public postsSubscription: Subscription

  public getPosts(){
    this.postsSubscription = this.flaskApiService.getPosts().subscribe(p => {
      console.log(p)
    })
  }

  ngOnInit() {
    this.getPosts();
  }
  
  ngOnDestroy(){
    this.postsSubscription.unsubscribe();
  }

}