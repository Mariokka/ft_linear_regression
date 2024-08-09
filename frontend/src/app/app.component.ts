import {Component} from '@angular/core';
import {PriceService} from "./service/price.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  estimatedPrice: number = 0;

  constructor(private priceService: PriceService) {
  }

  estimate(mileage: string) {
    if (mileage === '') {
      this.estimatedPrice = 0;
    } else {
      this.priceService.getPrice(parseInt(mileage)).subscribe((value) => {
          this.estimatedPrice = value;
        }
      )
    }
  }
}
