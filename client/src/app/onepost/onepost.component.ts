import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service'
@Component({
  selector: 'app-onepost',
  templateUrl: './onepost.component.html',
  styleUrls: ['./onepost.component.css']
})
export class OnepostComponent implements OnInit {
  id:number
  post
  constructor(private auth:AuthenticationService,public route:ActivatedRoute,private redirect: Router) { }

  ngOnInit(): void {
    console.log(this.route.snapshot.paramMap)
    const id = this.route.snapshot.paramMap.get('id');
    this.id=+id
    console.log(id)
    this.getPost()
    
  }

  getPost(){
    this.auth.getPostById(this.id)
    .subscribe((data)=>{
      this.post=data['post']
      // console.log(this.post)
      // console.log(this.post.title)
      // console.log(this.post.message['content'])
    })
    
  
  }

  deletePost(){
      this.auth.deletePost(this.id)
      .subscribe(data=>{
        window.alert("post deleted")
        this.redirect.navigateByUrl('/')
      })
  }





}
