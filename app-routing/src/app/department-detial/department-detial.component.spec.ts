import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DepartmentDetialComponent } from './department-detial.component';

describe('DepartmentDetialComponent', () => {
  let component: DepartmentDetialComponent;
  let fixture: ComponentFixture<DepartmentDetialComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DepartmentDetialComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DepartmentDetialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
