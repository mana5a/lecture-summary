import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { NgForm, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  result:any
  SERVER_URL = "http://localhost:5000/add";
  type = ['student','teacher'];
  model = new User('','', '', this.type[0]);
  registerForm: FormGroup;
  constructor(private httpClient: HttpClient) {}
  registered()
  {
    const formData = new FormData();
    console.log("what");

    console.log("hello", this.model.name, this.model.username, this.model.password, this.model.type);
   this.httpClient.post<any>(this.SERVER_URL,this.model).subscribe(
      (res) =>
      {
        console.log(res);
        console.log('here');
        this.result = res;
        if(res=="no")
          console.log("fail");
        else
          console.log("login");
      },
      (err) => console.log(err)
    );
  }}
