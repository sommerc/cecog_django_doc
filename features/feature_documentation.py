group_doc = {
      "Basic shape features":
        r"A collection to assess the objects shape. This group includes bla and blub",
      
      "Haralick features":
        r"The Haralick features aim at characterizing the texture of objects by means of joint"
        r"distribution of pixel value combinations."
        r"In histograms, one tries to analyze the frequency of certain grey level values in an"
        r"image. The inconvenience of this representation is that the spatial distribution of these"
        r"values is completely lost. One method to address this inconvenience is to record combinations"
        r"of pixel values at a certain distance. This can be done by the cooccurrence"
        r"matrix depending on distance d and angle \(\Phi\), which takes as element $c^{d,\phi}_{i,j}$ 
        r" the number of pixel pairs $x, y$ with distance $d$ at angle $\phi$, fulfilling $f(x) = i$ and $f(y) =j$"
        r"In order to obtain rotational invariance, the mean of the cooccurrence matrices is calculated for four 
        r"different angles ($\phi_i = 0^0, 45^0, 90^0, 145^0$). Let $P_{i,j}=\frac{c_{i,j}}{N}$ be the "
        r"cooccurrence probability for values $i$ and $j$ (for a given distance $d$ in all four angles) and let "
        r"$\mu = \sum_j j \sum_i P(i,j)$ the mean grey level value and $\sigma^2 = \sum_j (j-\mu)^2 \sum_i P(i,j)$"
        r"its variance. Then, the following features can be calculated from the averaged cooccurrence matrix",   
        
      "Basic intensity features":
        "",
        
      "Convex hull features":
        "",
        
      "Distance map features":
        "",
        
      "Granulometry features":
        "",
        
      "Moments":
        "",
        
      "Statistical geometric features":
        "",

      }

category_doc = {
    "circularity":
    "",
    
    "convexhull":
    "",
    
    "distance-map-dynamics":
    "",
    
    "geometry":
    "",
    
    "granulometry":
    "",
    
    "haralick":
    "",
    
    "haralick-normalized":
    "",
    
    "intensity":
    "",
    
    "intensity-normalized":
    "",
    
    "moments":
    "",
    
    "statistical-geometry":
    "",
    
    }

feature_doc = {
    "convexhull___average-clump-displacement":
      " ",

    "convexhull___area-ratio":
      " ",

    "convexhull___number-of-connected-components":
      " ",

    "convexhull___area-max-0":
      " ",

    "convexhull___area-max-1":
      " ",

    "convexhull___area-max-2":
      " ",

    "convexhull___area-mean":
      " ",

    "convexhull___rugosity":
      " ",

    "convexhull___number-of-large-connected-components":
      " ",

    "convexhull___area-variance":
      " ",

    "circularity___standard":
      r"is a rough estimation of the 'roundness' of the object: $circ = \frac{P}{2 \sqrt{\pi N}}$. It should be "
      "one for a perfect circle, becoming larger with decreasing similarity to a circle",

    "expansion___max":
      r"the maximal distance $\Delta_{max}$ between center of gravity and border pixels",

    "expansion___min":
      " ",

    "expansion___ratio":
      r"the ratio of minimal to maximal distance between center of gravity and border pixels (which takes 1 as a"
      "maximal value for a perfectly round object and 0 for an object with the center of gravity lying on its "
      "border (due to a strong concavity)",

    "distance-map-dynamics___number-of-maxima":
      " ",

    "distance-map-dynamics___highest-dynamic":
      " ",

    "eccentricity___":
      " ",

    "ellipse___ratio-axis":
      " ",

    "ellipse___major-axis":
      " ",

    "ellipse___minor-axis":
      " ",

    "granulometry___area-1":
      " ",

    "granulometry___area-2":
      " ",

    "granulometry___area-3":
      " ",

    "granulometry___area-5":
      " ",

    "granulometry___area-7":
      " ",

    "granulometry___volume-1":
      " ",

    "granulometry___volume-2":
      " ",

    "granulometry___volume-3":
      " ",

    "granulometry___volume-5":
      " ",

    "granulometry___volume-7":
      " ",

    "gyration___radius":
      " ",

    "gyration___ratio":
      " ",

    "haralick___ASM":
      r"Angular Second Moment (Energy), i.e. $\sum P_{i,j}^2$",

    "haralick___CON":
      r"Contrast (Inertia), i.e. $\sum P_{i,j}(i-j)^2$",

    "haralick___COR":
      r"Correlation, i.e. $- \sum \frac{(i-\mu)(j-\mu)}{\sigma^2} P(i,j)$",

    "haralick___COV":
      r"Coefficient of variation, i.e. $\frac{\sigma^2}{\mu}$",

    "haralick___DAV":
      r"Difference average, i.e. $\sum_k k \sum_{|i-j|=k} P(i,j)$ ",

    "haralick___ENT":
      r"Entropy, i.e. $- \sum P_{i,j} \log{P_{i,j}}$",

    "haralick___IDM":
      r"Inverse Difference Moment (Homogeneity), i.e. $\sum \frac{P_{i,j}}{1 + (i-j)^2}$",

    "haralick___PRO":
      r"Prominence, i.e. $\sum (i+j-2\mu)^4 P(i,j)$",

    "haralick___SAV":
      r"Sum average, i.e. the average of partial sums, subject to the condition $|i+j| = k$: $\sum_k k "
      r"\sum_{|i+j|=k} P(i,j)$",

    "haralick___SET":
      r"Sum entropy, i.e. $\sum_k \sum_{|i-j|=k} P(i,j) \log{\sum_{|i-j|=k} P(i,j)}$",

    "haralick___SHA":
      r"Shade, i.e. $\sum (i+j-2\mu)^3 P(i,j)$",

    "haralick___SVA":
      r"Sum variance, i.e. $\sum_k (k - SAV)^2 \sum_{|i-j|=k} P(i,j)$",

    "haralick___VAR":
      r"Variance, i.e. $\sum (i-\mu)^2 P(i,j)$",

    "haralick___average":
      r"Average $\mu$",

    "haralick___variance ":
      r"Variance $\sigma^2$",

    "haralick-normalized___ASM":
      " ",

    "haralick-normalized___CON":
      " ",

    "haralick-normalized___COR":
      " ",

    "haralick-normalized___COV":
      " ",

    "haralick-normalized___DAV":
      " ",

    "haralick-normalized___ENT":
      " ",

    "haralick-normalized___IDM":
      " ",

    "haralick-normalized___PRO":
      " ",

    "haralick-normalized___SAV":
      " ",

    "haralick-normalized___SET":
      " ",

    "haralick-normalized___SHA":
      " ",

    "haralick-normalized___SVA":
      " ",

    "haralick-normalized___VAR":
      " ",

    "haralick-normalized___average":
      " ",

    "haralick-normalized___variance ":
      " ",

    "circularity___robust-avg":
      r"is a more robust way of calculating circularity, as it does not rely on the perimeter, but on $\Delta_{max}$: "
      r"$irr = \frac{1 + \sqrt{\pi}\Delta_{max} }{\sqrt{N}} - 1$. The measure tends towards 0 for a perfect circle",

    "circularity___robust-max":
      r"is the same as irregularity, but $\Delta_{max}$ is replaced by the average difference $\overline{\Delta}$ "
      "between center of gravity and the border pixels",

    "statistical-geometry___CAREA_avgerage":
      " ",

    "statistical-geometry___CAREA_max":
      " ",

    "statistical-geometry___CAREA_sample_average":
      " ",

    "statistical-geometry___CAREA_sample_standard-deviation":
      " ",

    "statistical-geometry___DISP_avgerage":
      " ",

    "statistical-geometry___DISP_max":
      " ",

    "statistical-geometry___DISP_sample_average":
      " ",

    "statistical-geometry___DISP_sample_standard-deviation":
      " ",

    "statistical-geometry___INTERIA_avgerage":
      " ",

    "statistical-geometry___INTERIA_max":
      " ",

    "statistical-geometry___INTERIA_sample_average":
      " ",

    "statistical-geometry___INTERIA_sample_standard-deviation":
      " ",

    "statistical-geometry___IRGL_avgerage":
      " ",

    "statistical-geometry___IRGL_max":
      " ",

    "statistical-geometry___IRGL_sample_average":
      " ",

    "statistical-geometry___IRGL_sample_standard-deviation":
      " ",

    "statistical-geometry___NCA_avgerage":
      " ",

    "statistical-geometry___NCA_max":
      " ",

    "statistical-geometry___NCA_sample_average":
      " ",

    "statistical-geometry___NCA_sample_standard-deviation":
      " ",

    "statistical-geometry___TAREA_avgerage":
      " ",

    "statistical-geometry___TAREA_max":
      " ",

    "statistical-geometry___TAREA_sample_average":
      " ",

    "statistical-geometry___TAREA_sample_standard-deviation":
      " ",

    "algebraic-invariant___":
      " ",

    "intensity___avgerage":
      "the average grey value",

    "intensity___standard-deviation":
      r"the standard deviation of the grey values",

    "intensity___weighted-avgerage":
      r"the average, weighted by the distance between pixel and center of gravity: $\frac{1}{N}\sum |x - \overline{x}| f(x)$",

    "intensity___weighted-distance":
      r"average distance to the center of gravity: $\frac{1}{N}\sum |x - \overline{x}|$",

    "intensity___weighted-inverse-avgerage":
      r"the average, weighted by the inverse distance between pixel and center of gravity: $\frac{1}{N}\sum "
      r"\frac{f(x)}{|x - \overline{x}| + 1}$",

    "intensity-normalized___avgerage":
      r"the respective intensity features with normalization",

    "intensity-normalized___standard-deviation":
      r"the respective intensity features with normalization",

    "intensity-normalized___weighted-avgerage":
      r"the respective intensity features with normalization",

    "intensity-normalized___weighted-distance":
      r"the respective intensity features with normalization",

    "intensity-normalized___weighted-inverse-avgerage":
      r"the respective intensity features with normalization",

    "perimeter___":
      r"the object perimeter $P$ in pixels",

    "principle_gyration___ratio":
      " ",

    "principle_gyration___x":
      " ",

    "principle_gyration___y":
      " ",

    "area___":
      "the number of object pixels $N$ ",

    "skewness___x":
      " ",

    "skewness___y":
      " ",
}