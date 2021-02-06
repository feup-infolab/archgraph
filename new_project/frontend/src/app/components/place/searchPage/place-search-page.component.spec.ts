import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlaceSearchPageComponent } from './place-search-page.component';

describe('PlaceSearchPageComponent', () => {
  let component: PlaceSearchPageComponent;
  let fixture: ComponentFixture<PlaceSearchPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlaceSearchPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PlaceSearchPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
