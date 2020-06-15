import { BrowserModule } from '@angular/platform-browser';
import { NgModule, Component } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { ProfileComponent } from './profile/profile.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { AuthenticationService } from './authentication.service';
import { AuthGuardService } from './auth-guard.service';
import { NewpostComponent } from './newpost/newpost.component';
import { OnepostComponent } from './onepost/onepost.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { UpdateComponent } from './update/update.component';
import { combineAll } from 'rxjs/operators';
import { ChangepasswordComponent } from './changepassword/changepassword.component';
const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  {
    path: 'profile',
    component: ProfileComponent,
    canActivate: [AuthGuardService]
  },
  {path : 'new', component: NewpostComponent},
  {path: 'post/:id', component: OnepostComponent, canActivate: [AuthGuardService]},
  {path: 'reset_password', component: ResetPasswordComponent},
  {path:'post/:id/update', component: UpdateComponent},
  {path:'change_password/:email',component: ChangepasswordComponent}
];
@NgModule({
  declarations: [
    AppComponent,
    ProfileComponent,
    LoginComponent,
    RegisterComponent,
    HomeComponent,
    NewpostComponent,
    OnepostComponent,
    ResetPasswordComponent,
    UpdateComponent,
    ChangepasswordComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  providers: [AuthenticationService, AuthGuardService],
  bootstrap: [AppComponent]
})
export class AppModule { }
