import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { UploadComponent } from './upload/upload.component';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { TranscribeComponent } from './transcribe/transcribe.component';
import {ProgressBarModule} from "angular-progress-bar";
import { ProgressComponent } from './progress/progress.component'



@NgModule({
  declarations: [
    AppComponent,
    UploadComponent,
    TranscribeComponent,
    ProgressComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    ProgressBarModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
