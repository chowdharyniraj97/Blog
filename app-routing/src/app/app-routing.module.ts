import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {DepartmentListComponent} from './department-list/department-list.component'
import {EmployeeListComponent} from './employee-list/employee-list.component'


const routes: Routes = [
  {path:'department',  component:DepartmentListComponent},
  {path:'employee', component: EmployeeListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routing=[DepartmentListComponent,EmployeeListComponent]
