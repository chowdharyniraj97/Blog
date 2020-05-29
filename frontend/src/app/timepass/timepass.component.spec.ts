import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TimepassComponent } from './timepass.component';

describe('TimepassComponent', () => {
  let component: TimepassComponent;
  let fixture: ComponentFixture<TimepassComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TimepassComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TimepassComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
