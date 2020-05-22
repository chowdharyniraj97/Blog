import { TestBed } from '@angular/core/testing';

import { FlaskserviceapiService } from './flaskserviceapi.service';

describe('FlaskserviceapiService', () => {
  let service: FlaskserviceapiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FlaskserviceapiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
