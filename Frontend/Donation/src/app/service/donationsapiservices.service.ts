import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DonationsapiservicesService {

  constructor(private _http:HttpClient) { }

  // Providing the charities api
  charitiesApiUrl = 'https://donationappke.herokuapp.com/api/charities/';



  // Start of getting the specific charity
  getCharity(id:any) {
    let charityUrl = 'https://donationappke.herokuapp.com/api/charities/charities-id/' + id;

    return this._http.get<any>(charityUrl)
  }
  // End of charity by id call



  // Creating a function to grab the objects from the api
  charitiesProps():Observable<any> {
    return this._http.get(this.charitiesApiUrl)
  }


  
  donationsUrl = 'https://donationappke.herokuapp.com/api/donations/';

  donationsMade(userData:any):Observable<any> {
    return this._http.post(this.donationsUrl, userData);
  }

}