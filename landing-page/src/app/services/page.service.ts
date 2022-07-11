import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { observable } from 'rxjs';
import { HttpClient } from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PageService {
  API_URL = environment.production

  constructor(private http:HttpClient) { }
}
