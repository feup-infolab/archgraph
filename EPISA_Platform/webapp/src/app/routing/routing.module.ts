import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {CommonModule} from '@angular/common';
import {DocumentComponent} from '../components/document/document.component';
import {HomeComponent} from '../components/home/home/home.component';
import {ActorComponent} from '../components/actor/actor.component';
import {PlaceComponent} from '../components/place/place.component';
import {AdvancedSearchComponent} from '../components/search/advanced-search.component';
import {OrganizationComponent} from '../components/organization/organization.component';
import {RestorationComponent} from '../components/event/restoration/restoration.component';
import {SupportComponent} from '../components/event/support/support.component';
import {GenericComponent} from '../components/event/generic/generic.component';
import {DocSearchPageComponent} from '../components/document/searchPage/search/doc-search-page.component';
import {ActorSearchPageComponent} from '../components/actor/searchPage/actor-search-page.component';
import {EventSearchPageComponent} from '../components/event/searchPage/event-search-page.component';
import {PlaceSearchPageComponent} from '../components/place/searchPage/place-search-page.component';
import {OrgSearchPageComponent} from '../components/organization/searchPage/org-search-page.component';
import {HierarchyComponent} from '../components/search/hierarchy/hierarchy.component';
import {LoginComponent} from '../components/account/login/login.component';
import {RegisterComponent} from '../components/account/register/register.component';
import {CreateAndUpdateDocComponent} from '../components/document/createAndUpdate/create-and-update-doc.component';
import {AuthGuard} from '../_helpers/AutoGuard';
import {SearchComponent} from '../components/search/search/search.component';
import {ResultComponent} from '../components/document/searchPage/result/result.component';

const routes: Routes = [
  {
    path: 'home', component: HomeComponent, data: {
      title: 'Archgraph-HomePage'
    }
  },
  {
    path: 'login', component: LoginComponent, data: {
      title: 'Archgraph-Login'
    }
  },
  {
    path: 'register', component: RegisterComponent, data: {
      title: 'Archgraph-Register'
    }
  },
  {
    path: 'doc/:id', component: DocumentComponent
  },
  {
    path: 'createdoc', component: CreateAndUpdateDocComponent, data: {
      title: 'Archgraph-Create-Doc'
    }, canActivate: [AuthGuard]
  },
  {
    path: 'updatedoc/:id', component: CreateAndUpdateDocComponent, data: {
      title: 'Archgraph-Update-Doc'
    }, canActivate: [AuthGuard]
  },
  {
    path: 'searchdoc', component: DocSearchPageComponent, data: {
      title: 'Search for Doc'
    }
  },
  {
    path: 'search', component: SearchComponent, data: {
      title: 'Search Page'
    }
  },
  {
    path: 'result', component: ResultComponent, data: {
      title: 'Result Page'
    }
  },
  {
    path: 'actor/:id', component: ActorComponent, data: {
      title: 'Page Actor'
    }
  },
  {
    path: 'hierarchy', component: HierarchyComponent, data: {
      title: 'Hierarchy'
    }
  },
  {
    path: 'searchactor', component: ActorSearchPageComponent, data: {
      title: 'Search for Actor'
    }
  },
  {
    path: 'event/conservation_restoration/:id', component: RestorationComponent, data: {
      title: 'Dashboard'
    }
  },
  {
    path: 'event/support/:id', component: SupportComponent, data: {
      title: 'Dashboard'
    }
  },
  {
    path: 'event/generic/:id', component: GenericComponent, data: {
      title: 'Dashboard'
    }
  },
  {
    path: 'searchaevent', component: EventSearchPageComponent, data: {
      title: 'Search for Events'
    }
  },
  {
    path: 'place/:id', component: PlaceComponent, data: {
      title: 'Page Place'
    }
  },
  {
    path: 'searchplace', component: PlaceSearchPageComponent, data: {
      title: 'Search for places'
    }
  },
  {
    path: 'organization/:id', component: OrganizationComponent, data: {
      title: 'Page Organization'
    }
  },
  {
    path: 'searchorganization', component: OrgSearchPageComponent, data: {
      title: 'Search for Organizations'
    }
  },
  {
    path: 'advancedsearch', component: AdvancedSearchComponent, data: {
      title: 'Advanced Search'
    }
  },
  {
    path: '', redirectTo: '/home', pathMatch: 'full', data: {
      title: 'Archgraph-HomePage'
    }
  },
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})


export class RoutingModule {
}
