import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { EventService } from '../app.service';


@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  data: any;
  total_value: number = 0;
  title: string = "Hi"
  // private readonly _eventService: EventService = new EventService;

  constructor(
    private http: HttpClient, 
    private eventService: EventService
  ) { }

  ngOnInit(): void {
    this.http.get<any>('http://localhost:5000/product').subscribe(data => {
        this.data = data;
        this.total_value = 0;
    }) 
  }

  reduceQty(data: number, product: any): void {
    let currentValue = Number((<HTMLInputElement>document.getElementById("qty-"+data)).value) - 1;
    if (currentValue >= 0) {
      this.total_value = this.total_value - product.fields.price;
      this.eventService.broadcastMessage(this.total_value);
      (<HTMLInputElement>document.getElementById("qty-"+data)).value = String(currentValue);
    }
  }

  increaseQty(data: number, product: any): void {
    const currentValue = Number((<HTMLInputElement>document.getElementById("qty-"+data)).value) + 1;
    this.total_value = this.total_value + product.fields.price;
    this.eventService.broadcastMessage(this.total_value);
    (<HTMLInputElement>document.getElementById("qty-"+data)).value = String(currentValue);
  }
}
