import { Component, OnInit, AfterViewInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {timer} from 'rxjs';
import {take} from 'rxjs/operators';  


@Component({
  selector: 'app-progress',
  templateUrl: './progress.component.html',
  styleUrls: ['./progress.component.css']
})
export class ProgressComponent implements AfterViewInit {
  times=[0,10,20,30,40,50,60,70,80,90,100]
  constructor(private httpClient: HttpClient) { }
  result:any;
  SERVER_URL = "http://localhost:5000/progress";
  ngAfterViewInit() {

    timer(40, 100).pipe(
      take(100)).subscribe(x=>{
       // do here whatever you want to do
       this.httpClient.get<any>(this.SERVER_URL).subscribe(
        (res) => 
        {
          console.log(res);
          console.log("progress");
          this.result=res;
          
        },
        (err) => console.log(err)
         );
        
      })
      
  }
};