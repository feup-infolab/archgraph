import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css', '../../default.css']
})
export class SearchComponent implements OnInit {
  searchText: any;

  constructor() {
  }

  ngOnInit(): void {
  }

  search() {
    return;
  }
}

