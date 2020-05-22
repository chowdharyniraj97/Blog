import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

import { Post } from "./models/posts";

@Injectable({
  providedIn: 'root'
})
export class FlaskapiService {

  constructor(private httpClient: HttpClient) { }

  public server:string = "http://localhost:5000/";

  public getPosts(){
    return this.httpClient.get<Post>(this.server);
  }
}