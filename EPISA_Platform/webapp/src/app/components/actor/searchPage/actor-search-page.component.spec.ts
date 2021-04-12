import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActorSearchPageComponent } from './actor-search-page.component';

describe('ActorSearchPageComponent', () => {
  let component: ActorSearchPageComponent;
  let fixture: ComponentFixture<ActorSearchPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ActorSearchPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ActorSearchPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should createAndUpdate', () => {
    expect(component).toBeTruthy();
  });
});
