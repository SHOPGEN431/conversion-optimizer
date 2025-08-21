#!/usr/bin/env python3
"""
Conversion Rate Optimization Tool
Analyzes e-commerce product pages and provides specific recommendations to improve conversion rates.
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class Category(Enum):
    TRUST = "Trust & Credibility"
    UX = "User Experience"
    PRICING = "Pricing & Value"
    SOCIAL_PROOF = "Social Proof"
    CTA = "Call-to-Action"
    CONTENT = "Content Quality"
    TECHNICAL = "Technical"

@dataclass
class OptimizationRecommendation:
    category: Category
    priority: Priority
    title: str
    description: str
    impact: str
    implementation: str
    estimated_improvement: str
    code_example: Optional[str] = None

class ConversionOptimizer:
    def __init__(self):
        self.recommendations = []
        
    def analyze_page(self, page_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a product page and generate optimization recommendations."""
        self.recommendations = []
        
        # Analyze different aspects of the page
        self._analyze_trust_elements(page_data)
        self._analyze_user_experience(page_data)
        self._analyze_pricing_strategy(page_data)
        self._analyze_social_proof(page_data)
        self._analyze_call_to_actions(page_data)
        self._analyze_content_quality(page_data)
        self._analyze_technical_elements(page_data)
        
        return self._generate_report()
    
    def _analyze_trust_elements(self, page_data: Dict[str, Any]):
        """Analyze trust and credibility elements."""
        
        # Check for warranty information
        if "warranty" not in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.TRUST,
                priority=Priority.HIGH,
                title="Add Prominent Warranty Information",
                description="The page mentions warranty but it's not prominently displayed. Add a trust badge or warranty guarantee section.",
                impact="Increases customer confidence and reduces purchase anxiety",
                implementation="Add a warranty badge near the price and create a dedicated warranty section",
                estimated_improvement="15-25% increase in conversion rate",
                code_example="""
<div class="warranty-badge">
    <i class="fas fa-shield-alt"></i>
    <span>365-Day Warranty</span>
    <small>Full replacement or refund</small>
</div>
                """
            ))
        
        # Check for security badges
        if not any(badge in page_data.get("content", "").lower() for badge in ["ssl", "secure", "trusted"]):
            self.recommendations.append(OptimizationRecommendation(
                category=Category.TRUST,
                priority=Priority.MEDIUM,
                title="Add Security Trust Badges",
                description="Missing security indicators that build customer trust",
                impact="Reduces cart abandonment due to security concerns",
                implementation="Add SSL certificate badges, payment security icons, and trust seals",
                estimated_improvement="8-12% reduction in cart abandonment"
            ))
    
    def _analyze_user_experience(self, page_data: Dict[str, Any]):
        """Analyze user experience elements."""
        
        # Check for product images
        if page_data.get("image_count", 0) < 3:
            self.recommendations.append(OptimizationRecommendation(
                category=Category.UX,
                priority=Priority.HIGH,
                title="Add More Product Images",
                description="Limited product images reduce customer confidence in purchase decision",
                impact="Better product visualization leads to higher conversion rates",
                implementation="Add multiple angles, close-ups, and usage demonstration images",
                estimated_improvement="20-30% increase in conversion rate"
            ))
        
        # Check for product videos
        if "video" not in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.UX,
                priority=Priority.MEDIUM,
                title="Add Product Demo Video",
                description="Video demonstrations significantly improve conversion rates",
                impact="Shows product in action and builds confidence",
                implementation="Create a 30-60 second product demonstration video",
                estimated_improvement="25-40% increase in conversion rate"
            ))
    
    def _analyze_pricing_strategy(self, page_data: Dict[str, Any]):
        """Analyze pricing and value proposition."""
        
        # Check for price anchoring
        if "regular price" in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.PRICING,
                priority=Priority.MEDIUM,
                title="Improve Price Anchoring",
                description="Current price display could be more compelling",
                impact="Better price perception increases perceived value",
                implementation="Show original price crossed out, highlight savings amount",
                estimated_improvement="10-15% increase in conversion rate",
                code_example="""
<div class="pricing">
    <span class="original-price">$299.00</span>
    <span class="current-price">$249.00</span>
    <span class="savings">Save $50 (17% off)</span>
</div>
                """
            ))
        
        # Check for value proposition
        if len(page_data.get("benefits", [])) < 5:
            self.recommendations.append(OptimizationRecommendation(
                category=Category.PRICING,
                priority=Priority.HIGH,
                title="Strengthen Value Proposition",
                description="Limited benefits listed may not justify the price point",
                impact="Clear value proposition increases willingness to pay",
                implementation="Add more specific benefits and use cases",
                estimated_improvement="15-25% increase in conversion rate"
            ))
    
    def _analyze_social_proof(self, page_data: Dict[str, Any]):
        """Analyze social proof elements."""
        
        # Check for customer reviews
        if "customer reviews" not in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.SOCIAL_PROOF,
                priority=Priority.HIGH,
                title="Add Customer Reviews Section",
                description="Missing customer reviews and testimonials",
                impact="Social proof is crucial for building trust and credibility",
                implementation="Add a reviews section with star ratings and customer testimonials",
                estimated_improvement="20-35% increase in conversion rate",
                code_example="""
<div class="reviews-section">
    <h3>Customer Reviews</h3>
    <div class="rating">★★★★★ 4.8/5 (127 reviews)</div>
    <div class="testimonial">
        "Perfect for digitizing my old family videos. Easy to use and great quality!"
        - Sarah M.
    </div>
</div>
                """
            ))
        
        # Check for urgency/scarcity
        if "sold out" in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.SOCIAL_PROOF,
                priority=Priority.MEDIUM,
                title="Add Urgency Elements",
                description="Limited stock creates urgency but could be better communicated",
                impact="Creates fear of missing out and encourages immediate purchase",
                implementation="Add countdown timers, stock indicators, and urgency messaging",
                estimated_improvement="10-20% increase in conversion rate"
            ))
    
    def _analyze_call_to_actions(self, page_data: Dict[str, Any]):
        """Analyze call-to-action elements."""
        
        # Check for CTA button optimization
        if "add to cart" in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.CTA,
                priority=Priority.HIGH,
                title="Optimize CTA Button",
                description="Current CTA could be more compelling and action-oriented",
                impact="Better CTAs lead to higher click-through rates",
                implementation="Use action-oriented text, add urgency, and improve button design",
                estimated_improvement="15-25% increase in click-through rate",
                code_example="""
<button class="cta-button primary">
    <span class="main-text">Get Your Hi8 Player Now</span>
    <span class="sub-text">Free Shipping • 365-Day Warranty</span>
</button>
                """
            ))
        
        # Check for multiple CTAs
        if page_data.get("cta_count", 0) < 2:
            self.recommendations.append(OptimizationRecommendation(
                category=Category.CTA,
                priority=Priority.MEDIUM,
                title="Add Multiple CTAs",
                description="Single CTA may not capture all potential customers",
                impact="Multiple CTAs increase chances of conversion",
                implementation="Add CTAs at different scroll positions and in different formats",
                estimated_improvement="10-15% increase in conversion rate"
            ))
    
    def _analyze_content_quality(self, page_data: Dict[str, Any]):
        """Analyze content quality and structure."""
        
        # Check for product specifications
        if "specifications" not in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.CONTENT,
                priority=Priority.MEDIUM,
                title="Add Detailed Specifications",
                description="Missing technical specifications may reduce customer confidence",
                impact="Detailed specs help customers make informed decisions",
                implementation="Add a specifications table with all technical details",
                estimated_improvement="8-12% increase in conversion rate"
            ))
        
        # Check for FAQ section
        if "faq" not in page_data.get("content", "").lower():
            self.recommendations.append(OptimizationRecommendation(
                category=Category.CONTENT,
                priority=Priority.LOW,
                title="Add FAQ Section",
                description="FAQ section addresses common customer concerns",
                impact="Reduces customer service inquiries and builds confidence",
                implementation="Add common questions about compatibility, setup, and usage",
                estimated_improvement="5-10% increase in conversion rate"
            ))
    
    def _analyze_technical_elements(self, page_data: Dict[str, Any]):
        """Analyze technical aspects of the page."""
        
        # Check for mobile optimization
        if not page_data.get("mobile_optimized", False):
            self.recommendations.append(OptimizationRecommendation(
                category=Category.TECHNICAL,
                priority=Priority.HIGH,
                title="Improve Mobile Experience",
                description="Mobile optimization is crucial for modern e-commerce",
                impact="Better mobile experience increases mobile conversions",
                implementation="Ensure responsive design, fast loading, and mobile-friendly CTAs",
                estimated_improvement="20-30% increase in mobile conversion rate"
            ))
        
        # Check for page speed
        if page_data.get("load_time", 0) > 3:
            self.recommendations.append(OptimizationRecommendation(
                category=Category.TECHNICAL,
                priority=Priority.MEDIUM,
                title="Optimize Page Speed",
                description="Slow loading times increase bounce rates",
                impact="Faster pages lead to better user experience and higher conversions",
                implementation="Optimize images, minimize HTTP requests, use CDN",
                estimated_improvement="10-20% reduction in bounce rate"
            ))
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate a comprehensive optimization report."""
        
        # Group recommendations by category
        grouped_recommendations = {}
        for rec in self.recommendations:
            if rec.category.value not in grouped_recommendations:
                grouped_recommendations[rec.category.value] = []
            
            # Convert dataclass to dict and handle enum serialization
            rec_dict = asdict(rec)
            rec_dict['category'] = rec.category.value
            rec_dict['priority'] = rec.priority.value
            grouped_recommendations[rec.category.value].append(rec_dict)
        
        # Calculate priority distribution
        priority_counts = {}
        for rec in self.recommendations:
            priority_counts[rec.priority.value] = priority_counts.get(rec.priority.value, 0) + 1
        
        return {
            "analysis_date": datetime.now().isoformat(),
            "total_recommendations": len(self.recommendations),
            "priority_distribution": priority_counts,
            "recommendations_by_category": grouped_recommendations,
            "estimated_total_improvement": "40-60% increase in conversion rate",
            "implementation_priority": self._get_implementation_priority(),
            "quick_wins": [
                {
                    "title": win.title,
                    "description": win.description,
                    "impact": win.impact,
                    "implementation": win.implementation,
                    "estimated_improvement": win.estimated_improvement,
                    "priority": win.priority.value,
                    "category": win.category.value
                }
                for win in [r for r in self.recommendations if r.priority == Priority.HIGH][:3]
            ]
        }
    
    def _get_implementation_priority(self) -> List[str]:
        """Get prioritized implementation order."""
        high_priority = [r for r in self.recommendations if r.priority == Priority.HIGH]
        medium_priority = [r for r in self.recommendations if r.priority == Priority.MEDIUM]
        low_priority = [r for r in self.recommendations if r.priority == Priority.LOW]
        
        return [r.title for r in high_priority + medium_priority + low_priority]

def analyze_tapeplayers_page():
    """Analyze the specific TapePlayers.com page."""
    
    # Simulate page data based on the provided content
    page_data = {
        "url": "https://tapeplayers.com/products/canon-hi8-camcorder-tape-player-w-new-battery-usb-digitizing-software",
        "title": "Canon Hi8 Camcorder 8mm Tape Player w/ new battery, USB, digitizing software",
        "price": 249.00,
        "content": """
        Canon Hi8 Camcorder 8mm Tape Player w/ new battery, USB, digitizing software
        Regular price $249.00
        Qualifies for free shipping
        Free returns for 30 days
        1 year warranty
        Play and digitize 8mm, Hi8 tapes
        Shoot authentic vintage videos on tape
        Safely preserve your tapes at home
        Includes battery, blank tape, charger
        Guaranteed 100% working, free returns
        This bundle includes a fully tested and working 8mm camcorder, and all of the necessary components to playback your 8mm, Hi8 tapes on any TV or PC. You can also digitize your 8mm tapes over USB using any computer and preserve or share your memories.
        Includes battery and blank tape, so you're ready to start shooting vintage style videos that have a warm fuzzy look and feel. Many of our customers use these vintage camcorders for skate videos, hip-hop music videos, and to capture those iconic moments like weddings, travel, or a child's first camera.
        This product is backed our 365 day guarantee. Your product is eligible for a replacement or refund within 365 days of receipt if it does not work as expected. Get quick support for claims and free troubleshooting. The guarantee is in conjunction with our standard 30 day free return policy
        What's in the Box
        8mm/Hi8 camcorder
        Battery
        AC adapter, charger
        AV RCA cable
        AV to USB Adapter
        Blank tape
        Digitizing software
        """,
        "image_count": 4,
        "cta_count": 1,
        "load_time": 2.5,
        "mobile_optimized": True,
        "benefits": [
            "Play and digitize 8mm, Hi8 tapes",
            "Shoot authentic vintage videos on tape",
            "Safely preserve your tapes at home",
            "Includes battery, blank tape, charger",
            "Guaranteed 100% working, free returns"
        ]
    }
    
    optimizer = ConversionOptimizer()
    report = optimizer.analyze_page(page_data)
    
    return report

if __name__ == "__main__":
    # Analyze the TapePlayers.com page
    report = analyze_tapeplayers_page()
    
    # Print the report
    print("=" * 80)
    print("CONVERSION RATE OPTIMIZATION REPORT")
    print("=" * 80)
    print(f"Analysis Date: {report['analysis_date']}")
    print(f"Total Recommendations: {report['total_recommendations']}")
    print(f"Estimated Total Improvement: {report['estimated_total_improvement']}")
    print()
    
    print("PRIORITY DISTRIBUTION:")
    for priority, count in report['priority_distribution'].items():
        print(f"  {priority}: {count} recommendations")
    print()
    
    print("QUICK WINS (High Priority):")
    for i, win in enumerate(report['quick_wins'], 1):
        print(f"  {i}. {win.title}")
        print(f"     Impact: {win.impact}")
        print(f"     Estimated Improvement: {win.estimated_improvement}")
        print()
    
    print("DETAILED RECOMMENDATIONS BY CATEGORY:")
    for category, recommendations in report['recommendations_by_category'].items():
        print(f"\n{category.upper()}:")
        for rec in recommendations:
            print(f"  • {rec['title']} ({rec['priority']})")
            print(f"    {rec['description']}")
            print(f"    Impact: {rec['impact']}")
            print(f"    Estimated Improvement: {rec['estimated_improvement']}")
            print()
    
    # Save detailed report to JSON
    # Convert enum values to strings for JSON serialization
    serialized_recommendations = {}
    for category, recommendations in report['recommendations_by_category'].items():
        serialized_recommendations[category] = []
        for rec in recommendations:
            serialized_rec = {
                "title": rec['title'],
                "description": rec['description'],
                "impact": rec['impact'],
                "implementation": rec['implementation'],
                "estimated_improvement": rec['estimated_improvement'],
                "priority": rec['priority'],
                "category": rec['category']
            }
            if 'code_example' in rec:
                serialized_rec['code_example'] = rec['code_example']
            serialized_recommendations[category].append(serialized_rec)
    
    json_report = {
        "analysis_date": report['analysis_date'],
        "total_recommendations": report['total_recommendations'],
        "priority_distribution": report['priority_distribution'],
        "recommendations_by_category": serialized_recommendations,
        "estimated_total_improvement": report['estimated_total_improvement'],
        "implementation_priority": report['implementation_priority'],
        "quick_wins": [
            {
                "title": win.title,
                "description": win.description,
                "impact": win.impact,
                "implementation": win.implementation,
                "estimated_improvement": win.estimated_improvement,
                "priority": win.priority.value,
                "category": win.category.value
            }
            for win in report['quick_wins']
        ]
    }
    
    with open("conversion_optimization_report.json", "w") as f:
        json.dump(json_report, f, indent=2)
    
    print("Detailed report saved to 'conversion_optimization_report.json'") 