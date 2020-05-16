import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(public httpClient: HttpClient){}

  // Declare member variables for component
  boggle_board: any;
  cached_board: any = null;
  first_game_played: boolean = false;
  game_in_play: boolean = false;
  time: number;
  time_limit: number = 5;

  num_rounds: number = 0

  // Creates an httpClient observable and subscribes to the Boggle API
  playBoggle(){
    this.httpClient.get('http://127.0.0.1:5000/boggle').subscribe((res)=>{
        this.boggle_board = res['board'];
        this.game_in_play = true;
        this.first_game_played = true;
        this.num_rounds++;
        this.initializeTimer();
    });
  }

  initializeTimer(){
    this.time = this.time_limit;
    var id = setInterval(() => {
      this.time--;
      if (this.time == 0) {
        clearInterval(id);
        this.swap_boards();
        var time_to_reset = 5;
        var interval_reset = setInterval(() => {
          time_to_reset--;
          if (time_to_reset == 0) {
            clearInterval(interval_reset);
            this.swap_boards();
            this.game_in_play = false;
          }
        }, 1000);
      }
    }, 1000);
  }
  
  swap_boards(){
    this.boggle_board = [this.cached_board, this.cached_board = this.boggle_board][0];
  }

  title = 'bog';
}
