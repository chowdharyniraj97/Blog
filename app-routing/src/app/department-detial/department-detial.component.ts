import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap} from '@angular/router';

@Component({
  selector: 'app-department-detial',
  template: `
    <p>
      you cliked the department with id {{departmentid}}
    </p>
    <p>
      <button (click)="goPrevious()">Previous</button>
      <button (click)="goNext()">Next</button>
    </p>
  `,
  styles: [
  ]
})
export class DepartmentDetialComponent implements OnInit {
  departmentid;
  constructor(private activated:ActivatedRoute, private route : Router) { }

  ngOnInit() {
    //let id = parseInt(this.route.snapshot.paramMap.get('id'));
    this.activated.paramMap.subscribe((params: ParamMap) => {
      let id = parseInt(params.get('id'));
      this.departmentid = id;

    });
  }
  goPrevious() {
    let previousId = this.departmentid- 1;
    this.route.navigate(['/department', previousId]);
  }
  goNext() {
    let nextId = this.departmentid + 1;
    this.route.navigate(['/department', nextId]);
  }




}
