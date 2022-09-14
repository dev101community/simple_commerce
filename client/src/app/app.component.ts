import { Component } from '@angular/core';
import { EventService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private eventService: EventService) {}
  title = 'Simple Commerce';
  totalValue = 0;
  counter = 0;
  ngOnInit() {
    this.eventService.emitter.subscribe( message => {
      this.totalValue = message;
    });
    
  }

}
