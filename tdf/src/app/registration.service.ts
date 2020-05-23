import { Injectable } from '@angular/core';
import {User} from './user'
import {HttpClient} from '@angular/common/http'
@Injectable({
  providedIn: 'root'
})
export class RegistrationService {
  url="http://localhost:5000/register"
  constructor(public http : HttpClient ){ }

  register(user :User){
    return this.http.post<any>(this.url,user)
  }
}
