import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  data: any;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<any>('http://localhost:5000/product').subscribe(data => {
        this.data = data;
    }) 
  }

  reduceQty(data: number): void {
    const currentValue = Number((<HTMLInputElement>document.getElementById("qty-"+data)).value);
    (<HTMLInputElement>document.getElementById("qty-"+data)).value = String(currentValue - 1);
  }

  increaseQty(data: number): void {
    const currentValue = Number((<HTMLInputElement>document.getElementById("qty-"+data)).value);
    (<HTMLInputElement>document.getElementById("qty-"+data)).value = String(currentValue + 1);
  }

}
