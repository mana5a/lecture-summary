import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { NgForm, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  result:any
  SERVER_URL = "http://localhost:5000/check";
  type = ['student','teacher'];
  model = new User('','', '', this.type[0]);
  loginForm: FormGroup;
  constructor(private httpClient: HttpClient) {}
  clicked()
  {
    const formData = new FormData();
    console.log("hello", this.model.username, this.model.password, this.model.type);
   this.httpClient.get<any>(this.SERVER_URL+'?uname='+this.model.username+'&pass='+this.model.password+'&type='+this.model.type).subscribe(
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
