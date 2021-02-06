import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventSearchPageComponent } from './event-search-page.component';

describe('EventSearchPageComponent', () => {
  let component: EventSearchPageComponent;
  let fixture: ComponentFixture<EventSearchPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EventSearchPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EventSearchPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
