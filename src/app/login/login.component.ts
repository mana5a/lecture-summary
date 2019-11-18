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
  error_message = false;
  login_okay = false;
  SERVER_URL = "http://localhost:5000/check";
  type = ['Student','Teacher'];
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
        this.result = res;
        if(res=="no")
        {
          this.error_message = true;
          console.log("fail");
        }
        else
        {
          this.login_okay = true;
          console.log("login");
        }
      },
      (err) => console.log(err)
    );
  }

  notTriedLoggingIn(): boolean
  {
    if(this.error_message==false&&this.login_okay==false)
      return true;
    else
      return false;
  }
  loginOkay(): boolean
  {
    return this.login_okay;
  }
  errorMessage(): boolean
  {
    return this.error_message;
  }
}
