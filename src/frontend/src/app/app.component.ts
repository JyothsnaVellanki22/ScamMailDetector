import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { trigger, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  animations: [
    trigger('fadeInUp', [
      transition(':enter', [
        style({ opacity: 0, transform: 'translateY(20px)' }),
        animate('400ms ease-out', style({ opacity: 1, transform: 'translateY(0)' }))
      ]),
      transition(':leave', [
        animate('300ms ease-in', style({ opacity: 0, transform: 'translateY(10px)' }))
      ])
    ])
  ]
})
export class AppComponent {
  message: string = '';
  result: any = null;
  error: string = '';

  constructor(private http: HttpClient) { }

  checkSpam() {
    if (!this.message.trim()) return;

    this.error = '';
    this.result = null;

    // Use relative path for Vercel deployment (relies on vercel.json rewrite)
    // Locally, you might need a proxy or keep localhost if running separately.
    // Ideally, use environment variables. For this simple setup, we'll try relative.
    const apiUrl = window.location.hostname === 'localhost' ? 'http://localhost:8000/predict' : '/predict';

    this.http.post<any>(apiUrl, { message: this.message })
      .subscribe({
        next: (res) => this.result = res,
        error: (err) => {
          console.error(err);
          this.error = 'Error connecting to backend server. Is it running?';
        }
      });
  }
}
