import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service'
@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css']
})
export class UpdateComponent implements OnInit {

  constructor(private auth:AuthenticationService,public route:ActivatedRoute,private redirect : Router) { }
  id:number
  post
 new_post={
   'title':'',
   'content':''
 }
  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.id=+id
    console.log(id)
    this.getPost()
  }

  getPost(){
    this.auth.getPostById(this.id)
    .subscribe((data)=>{
      this.post=data['post']
      this.new_post.title=this.post.title;
      this.new_post.content=this.post.content;
      // console.log(this.post)
      // console.log(this.post.title)
      // console.log(this.post.message['content'])
    })
      
  }
  update(){
   
    this.auth.updatePost(this.id,this.new_post)
    .subscribe(data=>{
      console.log(data)
      this.redirect.navigateByUrl('/')
    })
  }
}
