import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-transcribe',
  templateUrl: './transcribe.component.html',
  styleUrls: ['./transcribe.component.css']
})
export class TranscribeComponent implements OnInit {

  SERVER_URL = "http://localhost:5000/generate";  
  constructor(private httpClient: HttpClient) { }

  ngOnInit() {
  }

  result:any
  generate() {
    this.httpClient.get<any>(this.SERVER_URL).subscribe(
      (res) => 
      {
        console.log(res);
        console.log("here");
        this.result=res;
      },
      (err) => console.log(err)
    );
  }
}