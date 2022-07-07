import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AboutviewComponent } from './aboutview/aboutview.component';
import { DonationviewComponent } from './donationview/donationview.component';
import { HomeviewComponent } from './homeview/homeview.component';
import { LoginviewComponent } from './loginview/loginview.component';
import { NavbarComponent } from './navbar/navbar.component';
import { PaymentviewComponent } from './paymentview/paymentview.component';
import { RegisterviewComponent } from './registerview/registerview.component';
import { WorkviewComponent } from './workview/workview.component';
import { UserRegisterService } from './service/user-register.service';
import { DonationsapiservicesService } from './service/donationsapiservices.service';

@NgModule({
  declarations: [
    AppComponent,
    AboutviewComponent,
    DonationviewComponent,
    HomeviewComponent,
    LoginviewComponent,
    NavbarComponent,
    PaymentviewComponent,
    RegisterviewComponent,
    WorkviewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    DonationsapiservicesService,
    UserRegisterService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
