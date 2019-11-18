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
  result: any;
  register_okay = false;
  error_message = false;
  username_okay=true;
  SERVER_URL_ADD = "http://localhost:5000/add";
  SERVER_URL_CHECK_USERNAME_EXISTS = "http://localhost:5000/username_exists";
  type = ['Student','Teacher'];
  model = new User('','', '', this.type[0]);
  registerForm: FormGroup;
  constructor(private httpClient: HttpClient) {}
  registered()
  {
    const formData = new FormData();
    this.httpClient.post<any>(this.SERVER_URL_ADD,this.model).subscribe(
      (res) =>
      {
        console.log(res);
        this.result = res;
        if(res=="no"||res=="username exists")
        {
          this.register_okay = false;
          this.error_message = true;
          console.log("fail");
        }
        else
        {
          this.register_okay = true;
          console.log("login");
        }
      },
      (err) => console.log(err)
    );
  }
  isUsernameOkay(): boolean {
    if(this.username_okay==true)
      return true;
    else
      return false;
  }
  isUsernameNotOkay(): boolean {
    if(this.username_okay==true)
      return false;
    else
      return true;
  }
  isUsernameTaken(e): any {
    var username = this.model.username;
    this.httpClient.post<any>(this.SERVER_URL_CHECK_USERNAME_EXISTS,username).subscribe(
    (res) =>
      {
        if(res=="True")
        {
          this.username_okay=false;
        }
        else
        {
          this.username_okay=true;
        }
      },
      (err) => 
      {
        console.log(err)
      }
    );
  }
  notTriedRegistering(): boolean
  {
    if(this.register_okay==false&&this.error_message==false)
      return true;
    else
      return false;
  }
  registerOkay(): boolean
  {
    return this.register_okay;
  }
  errorMessage(): boolean
  {
    return this.error_message;
  }
}
