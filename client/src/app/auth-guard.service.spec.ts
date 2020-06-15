import { TestBed } from '@angular/core/testing';

import { AuthGuardService } from './auth-guard.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {AuthenticationService} from './authentication.service';
import {RouterTestingModule} from '@angular/router/testing';

describe('AuthGuardService', () => {
  let service: AuthGuardService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports : [HttpClientTestingModule,RouterTestingModule],
      providers : [AuthenticationService,AuthGuardService]
    });
    service = TestBed.inject(AuthGuardService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
