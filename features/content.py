general_doc = {
      "Introduction": 
        "The CellCognition object features!"
       }

group_doc = {
      "Basic shape features":
        "A collection to assess the objects shape. This group includes bla and blub",
      
      "Haralick features":
        "Brief description of Haralick features",
        
      "Basic intensity features":
        "asdfasdfasdf",
        
      "Convex hull features":
        r"The convex hull of a binary image $X$ is the smallest convex set "
        r"containing $X$. Important features can be derived from the convex hull "
        r"and from the set difference." ,
        
      "Distance map features":
        "asdfasdfasdf",
        
      "Granulometry features":
        "asdfasdfasdf",
        
      "Moments":
        "",
        
      "Statistical geometric features":
        "",
      }

category_doc = {
    "circularity":
    "",
    
    "convexhull":
        r"The convex hull of a set $X$ (binary image) is the smallest convex set containing $X$. Important features can "
        r"be derived from the convex hull and from the set difference $D = Conv(X) \setminus X$. "
        "\n"
        r"To study the maximal areas of the connected components of $D$ is useful in order to find binuclear cell "
        r"nuclei for instance. A perfect binuclear cell should have two concavities of more or less the same "
        r"area. A trinuclear cell will have three concavities of similar size, if the three nuclei are positioned on "
        r"the corners of a triangle. If three nuclei are positioned in a row, the number of concavities is either higher "
        r"or the concavities have no symmetric size." 
        "\n"
        r"The size distribution of concavities is certainly a powerful feature. But we cannot conclude directly the "
        r"number of possibly involved cell nuclei. The reason is that a ``bended'' row of several nuclei results on one "
        r"side in one large concavity and on the other side in several small concavities. In order to deal with this "
        r"problem, it would be good, to be able to control the degree or size of concavity we are interested in. This "
        r"can be done by the use of granulometries.",
    
    "distance-map-dynamics":
    "",
    
    "geometry":
    "",
    
    "granulometry":
        r"Granulometry allows one to study the size distribution of objects (or"
        r"structures) in an image. For this, the image is successively simplified by operators which remove all (bright "
        r"or dark) structures up to a certain size. A record is kept of how much is removed from the image with each "
        r"filtering step, leading to a distribution of measurements $m_i$, which can be seen as size dependent texture "
        r"or shape descriptors.  More mathematically speaking, each anti-extensive (extensive), increasing and "
        r"absorptive operator $\psi$ with $\psi_0 f = f$ can be used for the definition of a granulometry "
        r"<a class='ref_link' href='#ref-serra:83'>[3]</a>. These properties make sure that the family of operators behaves like a set of sieves: with "
        r"increasing size, the sieves remove larger grains of the substance to be sieved. In practice, morphological "
        r"openings ($\gamma$: anti-extensive) and closings ($\phi$: extensive) are mostly used for this purpose. "
        r"In figure \ref{fig:granulometry}, the successive application of closings with increasing size are shown in "
        r"the first row: the concavities are successively filled. In the second row, the successive application of "
        r"openings with increasing size is shown: small details are successively removed."
        "\n"
        r"Let $\gamma_{sB}$ be a morphological opening with the structuringelement $B$ of size $s$. Then the family " 
        r"$\Gamma = \{ \gamma_{sB}\}$defines a series of operators which can be successively applied to theimage $f$. " 
        r"For each step, we record a measure (e.g. the sum of greylevel values) of what has been removed from the image. " 
        r"Hence, weobtain a list of measures $m_i = m(s_i)$ with $s_i \in \{s_1, s_2, s_3\ldots \}$. We have used the "
        r"volume and the area, where the imagevolume $Vol(\cdot)$ means the sum of grey levels and the area$Area(\cdot)$" 
        r"means the number of non zero pixels. "
        r"$$\begin{eqnarray} v^{\phi}_i &=& \frac{Vol(\phi_{s_{i+1}} f - \phi_{s_i} f)}{Vol(f)} \nonumber \\ "
        r"a^{\phi}_i &=& \frac{Area(\phi_{s_{i+1}} f - \phi_{s_i} f)}{Area(f)} \nonumber \\ "
        r"v^{\gamma}_i &=& \frac{Vol(\gamma_{s_i} f - \gamma_{s_{i+1}} f)}{Vol(f)} \nonumber \\ "
        r"a^{\gamma}_i &=& \frac{Area(\gamma_{s_i} f - \gamma_{s_{i+1}} f)}{Area(f)} \end{eqnarray}$$ "
        r"The features $v^{\phi}_i$ and $v^{\gamma}_i$ describe the texture in terms of size of dark and bright "
        r"substructures. If one of these valuesis particularly high, there were many substructures of this size inthe "
        r"object. We not that the last image in the second row of figure\ref{fig:granulometry} looks like an interphase. " 
        r"We can state, thatthe operators have removed and recorded the difference betweenprometaphase and interphase. " 
        r"However, there may be a problem with thelast structuring element: if the cell is too small, the last "
        r"openingwill eventually remove the whole cell. In this case, we would recordan abnormally high value. The " 
        r"features $a^{\gamma}_i$ and $a^{\phi}_i$ describe the irregularityof the shape. Whereas $a^{\phi}_i$ " 
        r"characterize the concavities (moreprecisely than the convex hull features, see the first row of "
        r"figure\ref{fig:granulometry}), the $a^{\gamma}_i$ describe prominent spikes.These features are inherently " 
        r"invariant to rotation, translation,and, due to the division by $Vol(f)$ and $Area(f)$, to scaling.  ",
    
    "haralick":
        r"The Haralick features aim at characterizing the texture of objects by means of joint"
        r"distribution of pixel value combinations."
        r"In histograms, one tries to analyze the frequency of certain grey level values in an"
        r"image. The inconvenience of this representation is that the spatial distribution of these"
        r"values is completely lost. One method to address this inconvenience is to record combinations"
        r"of pixel values at a certain distance. This can be done by the cooccurrence"
        r"matrix depending on distance $d$ and angle $\Phi$, which takes as element $c^{d,\phi}_{i,j}$ "
        r" the number of pixel pairs $x, y$ with distance $d$ at angle $\phi$, fulfilling $f(x) = i$ and $f(y) =j$ "
        r"In order to obtain rotational invariance, the mean of the cooccurrence matrices is calculated for four "
        r"different angles ($\phi_i = 0^0, 45^0, 90^0, 145^0$). Let $$P_{i,j}=\frac{c_{i,j}}{N}$$ be the "
        r"cooccurrence probability for values $i$ and $j$ (for a given distance $d$ in all four angles) and let "
        r"$\mu = \sum_j j \sum_i P(i,j)$ the mean grey level value and $\sigma^2 = \sum_j (j-\mu)^2 \sum_i P(i,j)$ "
        r"its variance. Then, the following features can be calculated from the averaged cooccurrence matrix.<br/><br/>"   
        r"The Haralick features have been calculated for the distances d = 1, 2, 4, 8. We have to "
        r"note that with increasing distance, the invariance of the features is no longer guaranteed. "
        r"For a discussion of the meaning of these features, please refer to "
        r"<a class='ref_link' href='#ref-held:05'>[1]</a>",
    
    "haralick-normalized":
        "same as haralick but on normalized image input",
    
    "intensity":
        "",
    
    "intensity-normalized":
        "same as intensity but on normalized image input",
    
    "moments":
        r"Moments and derived features have been initially defined to characterize distributions of values (like "
        r"histograms), but they can also be used as shape or texture descriptors. Discrete moments $m_{pq}$ are defined " 
        r" as: $$ \label{equ:moments} m_{pq} = \sum x^p y^q f(x,y)$$ with $f(x,y) \in \{0,1\}$ for shape descriptors "
        r"and $f(x,y)$ the grey level value for grey level descriptors. In pattern recognition tasks where objects are "
        r"to be characterized independently from their position and orientation, translation and rotation invariance are "
        r"required. This can be achieved by several means. One possibility is to use moment invariants <a class ='ref_link' href='#ref-hu:62'>[6]</a> as "
        r"features, i.e. to define polynomial combinations of moments which are invariant with respect to an affine "
        r"transformation. A second possibility is to find the principal axis of the pattern and to calculate the moments "
        r"with respect to this axis and the axis perpendicular to it. This corresponds to a rotation of the object in "
        r"such a way that its principal axis coincides with the x-axis. These moments are called standard moments "
        r"<a class ='ref_link' href='#ref-prokop:92'>[3]</a>."
        "\n"
        r"Furthermore, we can see from equation \ref{equ:moments}, that the moments can be written as $m_{pq} = " 
        r"\langle x^p y^q, f(x,y) \rangle$ with $\langle\cdot, \cdot\rangle$ the scalar product. This means that $m_{pq}$ is nothing else "
        r"than the projection of $f$ on the monomial $x^p y^q$. As the $x^p y^q$ are not orthogonal, the decomposition "
        r"is suboptimal in terms of redundancy. Therefore, the monomials can be replaced by orthogonal polynomials, "
        r"like Zernike or Legendre polynomials. A comparison of the resulting methods can be found in <a class='ref_link' href='#ref-teh:88'>[7]</a>. "
        r"In <a class='ref_link' href='#ref-prokop:92'>[3]</a>, the authors claim that standard moments give similar performance in pattern recognition "
        r"tasks as Zernike moments. We have not followed the approach of Zernike or Legendre moments.",
    
    "statistical-geometry":
        r"Statistical geometric features (or Levelset features) are shape features for different levelsets (i.e. results "
        r"of different thresholds) and, as such, texture features. For each of the following features, a distribution "
        r"of values is calculated according to the set of thresholds. For each of these distributions, the maximal "
        r"feature value, the average feature value, the sample mean and the sample standard deviation are calculated "
        r"as statistics (max_value, avg_value, sample_mean, sample_sd). Furthermore, all features are calculated on "
        r"the foreground and on the background after thresholding.",
    
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

github_prefix = "https://github.com/CellCognition/cecog/blob/master/"
feature_githublink = {
    "convexhull___average-clump-displacement": ("csrc/include/cecog/containers.hxx", 990,990),
    "convexhull___area-ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___number-of-connected-components": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-max-0": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-max-1": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-max-2": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-mean": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___rugosity": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___number-of-large-connected-components": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-variance": ("csrc/include/cecog/features.hxx", 990,990),
    "circularity___standard": ("csrc/include/cecog/features.hxx", 990,990),
    "expansion___max": ("csrc/include/cecog/features.hxx", 990,990),
    "expansion___min": ("csrc/include/cecog/features.hxx", 990,990),
    "expansion___ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "distance-map-dynamics___number-of-maxima": ("csrc/include/cecog/features.hxx", 990,990),
    "distance-map-dynamics___highest-dynamic": ("csrc/include/cecog/features.hxx", 990,990),
    "eccentricity___": ("csrc/include/cecog/features.hxx", 990,990),
    "ellipse___ratio-axis": ("csrc/include/cecog/features.hxx", 990,990),
    "ellipse___major-axis": ("csrc/include/cecog/features.hxx", 990,990),
    "ellipse___minor-axis": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-1": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-2": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-3": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-5": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-7": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-1": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-2": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-3": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-5": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-7": ("csrc/include/cecog/features.hxx", 990,990),
    "gyration___radius": ("csrc/include/cecog/features.hxx", 990,990),
    "gyration___ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___ASM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___CON": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___COR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___COV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___DAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___ENT": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___IDM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___PRO": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SET": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SHA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SVA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___VAR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___average": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___variance ": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___ASM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___CON": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___COR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___COV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___DAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___ENT": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___IDM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___PRO": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SET": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SHA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SVA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___VAR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___average": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___variance ": ("csrc/include/cecog/features.hxx", 990,990),
    "circularity___robust-avg": ("csrc/include/cecog/features.hxx", 990,990),
    "circularity___robust-max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "algebraic-invariant___": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___weighted-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___weighted-distance": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___weighted-inverse-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___weighted-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___weighted-distance": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___weighted-inverse-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "perimeter___": ("csrc/include/cecog/features.hxx", 990,990),
    "principle_gyration___ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "principle_gyration___x": ("csrc/include/cecog/features.hxx", 990,990),
    "principle_gyration___y": ("csrc/include/cecog/features.hxx", 990,990),
    "area___": ("csrc/include/cecog/features.hxx", 990,990),
    "skewness___x": ("csrc/include/cecog/features.hxx", 990,990),
    "skewness___y": ("csrc/include/cecog/features.hxx", 990,990),
}

parameter_doc = {
    "I" : "",
    "on": "",
    "distance": "",
    "angular-step": "",
    "operation": "",
    "radius": "",
                 }

reference_doc = {
    1:'neumann:06', 
    2:'held:05', 
    3:'prokop:92', 
    4:'serra:83', 
    5:'angulo_thesis:03',
    6:'hu:62', 
    7:'teh:88',
    8:'grimaud_thesis:91'}