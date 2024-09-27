import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map, Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class PriceService {

  constructor(private httpClient: HttpClient) { }

  getPrice(mileage: number): Observable<any> {
    return this.httpClient.get<any>(`http://127.0.0.1:5000/price?mileage=${mileage}`).pipe(
      map((response) => {
        return parseInt(response.price);
      })
    )
  }
}
