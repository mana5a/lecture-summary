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
  SERVER_URL_ADD = "http://localhost:5000/add";
  SERVER_URL_CHECK_USERNAME_EXISTS = "http://localhost:5000/username_exists";
  type = ['Student','Teacher'];
  model = new User('','', '', this.type[0]);
  registerForm: FormGroup;
  constructor(private httpClient: HttpClient) {}
  registered()
  {
    const formData = new FormData();
    console.log("what");

    console.log("hello", this.model.name, this.model.username, this.model.password, this.model.type);
    this.httpClient.post<any>(this.SERVER_URL_ADD,this.model).subscribe(
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
  }
  isUsernameTaken(): boolean {
    var username = this.model.username;
    var ret=false;
    this.httpClient.post<any>(this.SERVER_URL_CHECK_USERNAME_EXISTS,username).subscribe(
      (res) =>
      {
        if(res=="True")
          ret=true;
      },
      (err) => 
      {
        console.log(err)
      }
    );
    return ret;
  }

}
