import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrgSearchPageComponent } from './org-search-page.component';

describe('OrgSearchPageComponent', () => {
  let component: OrgSearchPageComponent;
  let fixture: ComponentFixture<OrgSearchPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OrgSearchPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OrgSearchPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
