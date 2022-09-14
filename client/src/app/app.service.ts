import { Injectable, EventEmitter, ViewChild, ElementRef } from '@angular/core';

@Injectable({
    providedIn: "root"
}
)
export class EventService {
  public emitter: EventEmitter<number> = new EventEmitter<number>();
  
  broadcastMessage(message: number): void {
    console.log("Emitting..." + message)
    this.emitter.emit(message);
  }

}