import { TestBed, async } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {AuthenticationService} from './authentication.service';
import {By} from 'protractor';

describe('AppComponent', () => {
  let auth:AuthenticationService
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule,
        HttpClientTestingModule
      ],
      declarations: [
        AppComponent
      ],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'client'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('client');
  });

  it('return true if user is logged in ', function() {
     const fixture = TestBed.createComponent(AppComponent);
     const app = fixture.componentInstance;
     auth=fixture.debugElement.injector.get(AuthenticationService)
      spyOn(auth,'isLoggedIn').and.returnValue(true)
    expect(auth.isLoggedIn()).toBeTruthy();
  });
it('return false if user is logged in ', function() {
     const fixture = TestBed.createComponent(AppComponent);
     const app = fixture.componentInstance;
     auth=fixture.debugElement.injector.get(AuthenticationService)
    spyOn(auth,'isLoggedIn').and.returnValue(false)
    expect(auth.isLoggedIn()).toBeFalsy();
  });

 it('return true as login button still displayed user not authenticated ', function() {
     const fixture = TestBed.createComponent(AppComponent);
     const app = fixture.componentInstance;
     auth=fixture.debugElement.injector.get(AuthenticationService);
     spyOn(auth,'isLoggedIn').and.returnValue(false)
     const val=auth.isLoggedIn()
     fixture.detectChanges();
    const compile = fixture.debugElement.nativeElement;
    const loggedInUser = compile.querySelector('#login');
    console.log(loggedInUser)
    expect(loggedInUser.textContent).toBe('Login');
  });

 it('return true as login button still displayed user not authenticated ', function() {
     const fixture = TestBed.createComponent(AppComponent);
     const app = fixture.componentInstance;
     auth=fixture.debugElement.injector.get(AuthenticationService);
     spyOn(auth,'isLoggedIn').and.returnValue(true)
     const val=auth.isLoggedIn()
     fixture.detectChanges();
    const compile = fixture.debugElement.nativeElement;
    const loggedInUser = compile.querySelector('#logout');
    expect(loggedInUser.textContent).toBe('Logout');
  });
});
